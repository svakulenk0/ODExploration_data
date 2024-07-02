# Open Data Exploration Dataset

## Summary

26 chat-based student conversation transcripts about the content of the two Austrian open data portals:

* [data.gv.at](https://www.data.gv.at) (13 conversations)
* [opendataportal.at](https://www.opendataportal.at) (13 conversations)


16 conversations included elements of exploration with listing of available categories, dataset samples, facets, etc., while other 10 were purely search-based interactions focused on addressing specific questions directly. 24 conversation transcripts as samples with a successful interacion outcome, i.e. resulting in satisfied information need and positive user feedback, 2 - unsuccessful interacion outcome.


## Annotations

The transcripts are manually annotated with the dialog act types (intents/responses) and the speaker identifier (agent/User). The new lines separators were inserted within the same message to indicate the spans of text with different message types.


Annotation template: message_type>speaker_turn>message
e.g. greeting>E>Hi?

We differentiate between 15 different dialog act types, which correspond to the basic  operations available for data exploration.

1. Dialog acts used by **both** Seeker and Intermediary:
   
        * greeting(), indicates common start of the conversation, e.g. "hello"
        * confirm(), explicitly confirms the direction for exploration
        * verify(), prompts to confirm the direction for exploration or the results
        * success(), indicates end of the conversation with a successful outcome
        * prompt(link), suggests/asks for a direct link to the dataset

    Dialog acts of an **Intermediary**:

        * prompt(keywords), indicates a general information request
        * list(keywords), indicates available options on different levels (attributes, items)
        * bool(data), reports existance of the requested set of items (datasets/columns/attributes)
        * top(keywords), reports the top (most frequent) items (rows/attributes)
        * count(data), reports the count of items (rows/datasets/attributes)
        * link(dataset), reports the direct link to a dataset


    Dialog acts of a **Seeker**:
    
        * question(data), indicates a general information request, e.g. "what data do you have?"
        * set(keywords), indicates the choice of a specific direction for exploration, e.g. "have you got smth on population statistics?"
        * reject(), explicitly rejects the direction for exploration
        * more(), indicates a request for more items from the same equivalence class



2. Dialog turn separators:

* A for the agent utterance
* U for the user utterance

3. [[]] indicates concept span

Codes for span annotations:

* [[]]H* - greeting;
* [[]]G* - question about the data availability/need;
* [[]]F* - attribute (facet) as a selection option for the next exploration direction, e.g. category;
* [[]]E* - entity option (facet value) for exploration, e.g. finance;
* [[]]Q* - cardinality of the corresponding item set;
* [[]]R* - unique identifier of an item, e.g. title or link to the dataset;
* [[]]+* - positive feedback;
* [[]]-* - negative feedback.

Average number of concepts per utterance 2

Maximum number of concepts per utterance 16


## Process models

Produced with ProM: Inductive Visual Miner and Declarative model?


## License  
  
All work in this repository is under the [MIT license](LICENSE)

## Acknowledgement  

If you find this work useful, feel free to cite us:

```
@article{DBLP:journals/corr/abs-2012-03704,
  author       = {Svitlana Vakulenko and
                  Vadim Savenkov and
                  Maarten de Rijke},
  title        = {Conversational Browsing},
  journal      = {CoRR},
  volume       = {abs/2012.03704},
  year         = {2020},
  url          = {https://arxiv.org/abs/2012.03704},
}

```
