# PageSpeed Batch Analyser

- Follow instructions at [https://developers.google.com/speed/docs/insights/v5/get-started](https://developers.google.com/speed/docs/insights/v5/get-started) to set up API key. Update API_KEY in *main.py*.
- Install aiohttp dependency

    ```bash
    pip install aiohttp
    ```

- To run, include path to file as command line argument. For example,

    ```bash
    python ./main.py ./testURLs.txt
    ```