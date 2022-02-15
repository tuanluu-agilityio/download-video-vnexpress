# download-videos-vnexpress
Download videos from site news vnexpress.net

### Install
```
$ cd vnexpress
$ pip install -r requirements.txt
```

```mermaid
flowchart TD
    A[Install] --> B{Are you Sure?};
    B -- Yes --> C[pip install -r requirements.txt];
    B -- No --> D[Quit];
    C ----> E[Enjoy your weekend!];
    D ----> E[Enjoy your weekend!];
```

### How to run
```
$ scrapy crawl video_vnexpress
```
