# DialogCorpus
A large scale dialog corpus for training the Next-Gen Dialog System.

## How to Use?

First download the repository.
```bash
# download
git clone https://github.com/qywu/DialogCorpus.git
cd DialogCorpus

# download data for the specific task
python daily_dialog/download_data.py
# process the data
python daily_dialog/process_data.py
# the processed data is stored as the {folder_name}.json
vi daily_dialog/data/daily_dialog.json
```

## Detailed Dialog Processing for each dataset:

* Daily Dialog
    * Removed tokenization space for punctuations

* Persona Chat
    * Used huggingface's version [[link]](https://s3.amazonaws.com/datasets.huggingface.co/personachat/personachat_self_original.json)
    * Recovered lower cased utterances
    * Removed tokenization space for punctuations

* Cornell Movie Corpus
    * Ignored UTF-8 Errors
    * Extracted Names

* Task Master
    * Nothing specific

* [CCPE] (https://ai.google/tools/datasets/coached-conversational-preference-elicitation)
    * Nothing specific

* [Frames](https://www.microsoft.com/en-us/research/project/frames-dataset/)
    * Nothing specific

* [Chit-Chat Challenge](https://github.com/BYU-PCCL/chitchat-dataset)
    * Nothing specific

* [Self-dialogue](https://github.com/jfainberg/self_dialogue_corpus)
    * Nothing specific

* [Schema Dialog](https://github.com/google-research-datasets/dstc8-schema-guided-dialogue)
    * Nothing specific

Links


* [Daily Dialog](http://yanran.li/dailydialog) [[link]](https://github.com/qywu/DialogCorpus/tree/master/daily_dialog)

* [Conversational flow in Oxford-style debates](http://tisjune.github.io/research/iq2) [[link]](https://github.com/qywu/DialogCorpus/tree/master/debates)

* [Persona-chat](https://github.com/facebookresearch/ParlAI/tree/master/parlai/tasks/convai2) [[Google Drive](https://drive.google.com/open?id=1VacuNTaQo9-tXv52XaHczPxXejRuJk9T)] 


Thanks for Jing Gu processing the data. If you have questions, you can contact jkgu@ucdavis.edu.