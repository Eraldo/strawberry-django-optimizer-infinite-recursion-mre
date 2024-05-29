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
query ColorWithFruits {
  colors(first: 1) {
    totalCount
    edges {
      node {
        id
        fruits(filters: {name: {startsWith: "Straw"}}) {
          edges {
            node {
              id
              name
            }
          }
        }
      }
    }
  }
  
  fruits(filters: {name: {startsWith: "Straw"}}) {
    totalCount
  }
}
```