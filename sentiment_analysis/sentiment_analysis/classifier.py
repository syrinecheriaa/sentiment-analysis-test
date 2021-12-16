
from .data_reader import read_text
from .const import path_checkpoint_file, path_index_to_target
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from torch.utils.data import  DataLoader
import os, json, torch
import numpy as np


class SentimentAnalysisDataset(torch.utils.data.Dataset):       

    def __init__(self, content, tokenizer):
        self.text = content
        self.encodings = tokenizer(content, truncation=True, padding=True, max_length=64)
    
    def __getitem__(self, idx):
        item = {key:torch.tensor(val[idx]) for key, val in self.encodings.items()}
        return item
    
    def __len__(self):
        return len(self.text)


class Classifier():
    def __init__(self):
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.model_name = f"cardiffnlp/twitter-xlm-roberta-base-sentiment"
        self.model = self.load_model()
        self.tokenizer = self.load_tokenizer()
        self.index_to_target = self.load_index_to_target()
        
    def load_index_to_target(self):
        with open(path_index_to_target) as f:
            dictionary = json.load(f)
        return dictionary

    def load_model(self):
        model = AutoModelForSequenceClassification.from_pretrained(self.model_name)
        model.load_state_dict(torch.load(path_checkpoint_file, map_location=torch.device(self.device)))
        model.eval()
        model.to(self.device)
        return model

    def load_tokenizer(self):
        return AutoTokenizer.from_pretrained(self.model_name)

    def create_data_loader(self, content):
        params = {'batch_size': 8,
                    'shuffle': False,
                    'num_workers': 0
                }
        
        return DataLoader(dataset, **params)

    def predict(self, content):

        texts = read_text(content)
        dataloader = self.create_data_loader(texts)
        outputs = self.get_results(dataloader)
        return outputs

    def get_results(self, dataloader):
        all_results = []
        for _, data in enumerate(dataloader):
            input_ids = data['input_ids'].to(self.device, dtype = torch.long)
            attention_mask = data['attention_mask'].to(self.device, dtype = torch.long)
            outputs = self.model(input_ids, attention_mask)            
            all_results.extend(torch.nn.Softmax(dim=1)(outputs.logits).cpu().detach().numpy().tolist())
        return self.get_categories_from_idx(np.array(all_results))
    
    def get_categories_from_idx(self, all_results):
        
        return [self.index_to_target[str(index)] for index in np.argmax(all_results, axis=1)]