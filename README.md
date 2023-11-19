## **How to Run the App:**

*Prerequisites*

 - ElasticSearch Local Setup
 - Python 3+
 - Flask

**STEPS**
1. We need to first clean the ap89 dataset to index them in elastic search.
2. "dataprep/fileparser.py" is a parser written for this dataset. So just change the collection location and start cleaning.
![enter image description here](https://i.ibb.co/VLswY4x/Screenshot-2023-11-18-171718.png)
3. You will see the process like this 
![enter image description here](https://i.ibb.co/NNRMYZ5/Screenshot-2023-11-18-164233.png)

4. After the parsing, a JSON file named "parsed_file.json" will be created.
5. To index this data I have written an indexer named "dataprep/esindexer.py"
6. Before running it make sure you have installed elasticsearch python client from :https://elasticsearch-py.readthedocs.io/en/v8.11.0/
7. Edit the config below according to your ES instance
![enter image description here](https://i.ibb.co/FxfYGGj/indexer-config.png)We are creating "ap89" index in ES make sure you don't have a index named this or just comment the line out

8. If everything works perfectly you will see the indexing process like below:
![enter image description here](https://i.ibb.co/1nvJPrw/Screenshot-2023-11-15-174426.png)

9. Lets fireup out Frontend now. Its a flask based app so make sure you install flask before running it
10. Just like step 7 edit the required ES config details in "index.py" and Run the "index.py" the deployment will start.
11. Its screenshots below:
![enter image description here](https://i.ibb.co/K9Q5DmM/Screenshot-2023-11-18-163948.png)Homepage

![enter image description here](https://i.ibb.co/D1rjbbj/Screenshot-2023-11-18-164012.png)SeachResults
