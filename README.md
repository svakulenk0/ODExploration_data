# Open Data Exploration Dataset

## Summary

26 chat-based student conversation transcripts about the content of the two Austrian open data portals:

* [data.gv.at](https://www.data.gv.at) (13 conversations)
* [opendataportal.at](https://www.opendataportal.at) (13 conversations)


16 conversations included elements of exploration with listing of available categories, dataset samples, facets, etc., while other 10 were purely search-based interactions focused on addressing specific questions directly.


## Annotations

The transcripts are manually annotated with the message types (intents/responses) and the speaker identifier (Expert/User). The new lines separators were inserted within the same message to indicate the spans of text with different mesage types.


Annotation template: message_type>speaker_turn>message
e.g. greeting>E>Hi?

We differentiate between 15 different message types (intents and responds), which correspond to the basic  operations available for data exploration.

1. Message types produced by **both** (user and expert) are in range:
   
        * greeting(), indicates common start of the conversation, e.g. "hello"
        * confirm(), explicitly confirms the direction for exploration
        * verify(), prompts to confirm the direction for exploration or the results
        * success(), indicates end of the conversation with a successful outcome
        * prompt(link), suggests/asks for a direct link to the dataset

    utterances and responses produced by **expert**:

        * prompt(keywords), indicates a general information request
        * list(keywords), indicates available options on different levels (facets, attributes, datasets, columns)
        * bool(data), reports existance of the requested set of items (datasets/columns/attributes)
        * top(keywords), reports the top (most frequent) items (rows/attributes)
        * count(data), reports the count of items (rows/datasets/attributes)
        * link(dataset), reports the direct link to a dataset


    intents and responses by **user**:
    
        * question(data), indicates a general information request, e.g. "what have you got"
        * set(keywords), indicates the choice of a specific direction for exploration, e.g. "have you got smth on population statistics"
        * reject(), explicitly rejects the direction for exploration
        * more(), indicates a request for more items from the same equivalence class




2. Dialog turn separators:

* E for the expert utterance
* U for the user utterance

3. [[concept]] mark-up is used to build the templates with the ontology concepts used as variables


## License  
  
All work in this repository is under the [MIT license](LICENSE)
