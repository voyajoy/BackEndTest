```bash
cd source
docker build --tag=gitradar .
docker run -it --rm --publish=127.0.0.1:8080:8080 gitradar
```

#API

## List of authors
``` 
GET /api/authors/
```

## Commits from an author

```
GET /api/commits/author/{{AUTHOR_ID}}
```

## Mark commit as read or unread
``` 
GET /api/commit/{{COMMIT_ID}}/{{STATUS}}/
```

STATUS is status of commit:
 'R' - read
 'U' - unread 