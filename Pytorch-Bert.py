import numpy as np
import torch
from transformers import BertTokenizer, BertConfig, BertForMaskedLM, BertForNextSentencePrediction
from transformers import BertModel

model_name = 'bert'
MODEL_PATH = './bert'
# 通过词典导入分词器
tokenizer = BertTokenizer.from_pretrained(model_name)
# 导入配置文件
model_config = BertConfig.from_pretrained(model_name)
# 修改配置
model_config.output_hidden_states = True
model_config.output_attentions = True
# 通过配置和路径导入模型
bert_model = BertModel.from_pretrained(MODEL_PATH, config=model_config)
# encode仅返回input_ids
print(tokenizer.encode('我儿莫慌'))
# encode_plus返回所有编码信息
sen_code = tokenizer.encode_plus('这个故事没有终点', '正如星空没有彼岸')
print(sen_code)
# 将input_ids转化回token
print(tokenizer.convert_ids_to_tokens(sen_code['input_ids']))
# 对编码进行转换，以便输入Tensor
token_tensor = torch.tensor([sen_code['input_ids']])
segment_tensors = torch.tensor([sen_code['token_type_ids']])

bert_model.eval()

# 编码
with torch.no_grad():
    outputs = bert_model(token_tensor, token_type_ids=segment_tensors)
    encoded_layers = outputs
    print(encoded_layers[0].shape, encoded_layers[1].shape, encoded_layers[2][0].shape, encoded_layers[3][0].shape)

# 任务1：遮蔽语言模型
samples = ['[CLS] 中国的首都是哪里？ [SEP] 北京是 [MASK] 国的首都。 [SEP]']
tokenizer_text = [tokenizer.tokenize(i) for i in samples]
input_ids = [tokenizer.convert_tokens_to_ids(i) for i in tokenizer_text]
input_ids = torch.LongTensor(input_ids)

model = BertForMaskedLM.from_pretrained(model_name, cache_dir='./')
model.eval()

outputs = model(input_ids)
prediction_scores = outputs[0]
sample = prediction_scores[0].detach().numpy()

pred = np.argmax(sample, axis=1)
print(tokenizer.convert_ids_to_tokens(pred))
print(tokenizer.convert_ids_to_tokens(pred)[14])

# 任务2：句子预测任务
samples = ['[CLS]今天天气怎么样？[SEP]今天天气很好！[SEP]', '[CLS]明明是我先来的！[SEP]我喜欢吃西瓜！[SEP]']
tokenized_text = [tokenizer.tokenize(i) for i in samples]
input_ids = [tokenizer.convert_tokens_to_ids(i) for i in tokenized_text]
tokens_tensor = torch.LongTensor(input_ids)

model = BertForNextSentencePrediction.from_pretrained(model_name, cache_dir='./')
model.eval()

outputs = model(tokens_tensor)
seq_relationship_scores = outputs[0]
sample = seq_relationship_scores.detach().numpy()

pred = np.argmax(sample, axis=1)
print(pred)

"""
outputs:
[2769, 1036, 5811, 2707]
{'input_ids': [6821, 702, 3125, 752, 3766, 3300, 5303, 4157, 3633, 1963, 3215, 4958, 3766, 3300, 2516, 2279], 'token_type_ids': [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]}
['这', '个', '故', '事', '没', '有', '终', '点', '正', '如', '星', '空', '没', '有', '彼', '岸']
torch.Size([1, 16, 768]) torch.Size([1, 768]) torch.Size([1, 16, 768]) torch.Size([1, 12, 16, 16])
['，', '中', '国', '的', '首', '都', '是', '哪', '里', '？', '。', '北', '京', '是', '中', '国', '的', '首', '都', '。', '。']
中
[0 0]

"""

 
