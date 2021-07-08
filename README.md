# PageSpeed Batch Analyser

- Follow instructions at [https://developers.google.com/speed/docs/insights/v5/get-started](https://developers.google.com/speed/docs/insights/v5/get-started) to set up API key. Update API_KEY in *main.py*.
- Install requests and aiohttp dependency

    ```bash
    pip install requests
    pip install aiohttp
    ```

- On Windows, uncomment in *main.py* line 62 before running

    ```python
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    ```

- To run, include path to file as command line argument. For example,

    ```bash
    python ./main.py ./testURLs.txt
    ```
