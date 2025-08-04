import pandas as pd
import torch
from datasets import Dataset
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    TrainingArguments,
    Trainer
)
from sklearn.metrics import f1_score, accuracy_score

MODEL_NAME = "neuralmind/bert-base-portuguese-cased"
DATASET_PATH = "dataset.csv"
OUTPUT_DIR = "./stride-finetuned-model"

df = pd.read_csv(DATASET_PATH)
labels = [label for label in df.columns if label != 'text']
id2label = {idx: label for idx, label in enumerate(labels)}
label2id = {label: idx for idx, label in enumerate(labels)}

dataset = Dataset.from_pandas(df)

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

def preprocess_data(examples):
    encoding = tokenizer(examples["text"], padding="max_length", truncation=True, max_length=128)
    
    encoding["labels"] = [
        [1.0 if examples[label][i] else 0.0 for label in labels]
        for i in range(len(examples["text"]))
    ]
    return encoding

encoded_dataset = dataset.map(preprocess_data, batched=True, remove_columns=dataset.column_names)

model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_NAME, 
    problem_type="multi_label_classification",
    num_labels=len(labels),
    id2label=id2label,
    label2id=label2id
)

training_args = TrainingArguments(
    output_dir=OUTPUT_DIR,
    num_train_epochs=15,
    per_device_train_batch_size=4,
    learning_rate=5e-5,
    save_strategy="epoch",
    logging_steps=1,
    report_to="none"
)

def compute_metrics(p):
    preds = p.predictions[0] if isinstance(p.predictions, tuple) else p.predictions
    sigmoid = torch.nn.Sigmoid()
    probs = sigmoid(torch.Tensor(preds))
    y_pred = (probs > 0.5).int().numpy()
    y_true = p.label_ids
    
    f1_micro_average = f1_score(y_true=y_true, y_pred=y_pred, average='micro')
    accuracy = accuracy_score(y_true, y_pred)
    
    return {"f1": f1_micro_average, "accuracy": accuracy}

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=encoded_dataset,
    tokenizer=tokenizer,
    compute_metrics=compute_metrics
)

print("Iniciando o fine-tuning...")
trainer.train()

trainer.save_model(OUTPUT_DIR)
print(f"Modelo salvo em {OUTPUT_DIR}")