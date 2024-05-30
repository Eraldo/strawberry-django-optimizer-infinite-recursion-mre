Superuser:
- Username: "admin"
- Pasword: "admin"

Start app:
```
python manage.py runserver 
```

Go to Playground:
```
http://127.0.0.1:8000/graphql
```

Enter query:
```graphql
query OrderedFruits {
  fruits {
    totalCount
    edges {
      node {
        id
        name
      }
    }
  }
}
```

=> Confirm the error message. ;)