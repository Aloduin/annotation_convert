
import json


def get_class_word(bio_tag: str) -> str:
    if bio_tag.startswith('B-') or bio_tag.startswith('I-'):
        return bio_tag[2:]
    elif bio_tag == 'O':
        return bio_tag
    else:
        raise ValueError
    
    
def main():
    dataset_path = r"E:/Datasets/mpv_NER_dataset.json"
    with open(dataset_path, 'r', encoding='utf-8') as f:
        dataset = json.load(f)
    io_labels = []
    labels = dataset['labels']
    for label in labels:
        label = [get_class_word(l) for l in label]
        io_labels.append(label)
        
    cnt_data = len(io_labels)
    
    
    train_data = [[(t, l) for t, l in zip(tok, lab)] for tok, lab in zip(dataset['tokens'][:int(cnt_data * 0.7)], io_labels[:int(cnt_data * 0.7)])]
    val_data = [
        [
            (t, l) for t, l in zip(tok, lab)
        ]
        for tok, lab in zip(
            dataset['tokens'][int(cnt_data * 0.7): int(cnt_data * 0.8)], 
            io_labels[int(cnt_data * 0.7): int(cnt_data * 0.8)]
        )
    ]
    test_data = [
        [
            (t, l) for t, l in zip(tok, lab)
        ]
        for tok, lab in zip(
            dataset['tokens'][int(cnt_data * 0.8):], 
            io_labels[int(cnt_data * 0.8):]
        )
    ]
    with open('./data/train.txt', 'w', encoding='utf-8') as f:
        for sent in train_data:
            for w in sent:
                f.write(w[0])
                f.write("\t")
                f.write(w[1])
                f.write('\n')

            f.write('\n')
    
    with open('./data/val.txt', 'w', encoding='utf-8') as f:
        for sent in val_data:
            for w in sent:
                f.write(w[0])
                f.write("\t")
                f.write(w[1])
                f.write('\n')

            f.write('\n')      
    
    
    with open('./data/test.txt', 'w', encoding='utf-8') as f:
        for sent in test_data:
            for w in sent:
                f.write(w[0])
                f.write("\t")
                f.write(w[1])
                f.write('\n')
            f.write('\n')
            
            
if __name__ == '__main__':
    main()