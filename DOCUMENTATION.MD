# `SAMARITAN.AI` Documentation

### Basics

- `POST` request to `https://samaritan-ai.herokuapp.com/api/`

- **Headers**
	- `auth_key: TheDayTheWorldWentAway`
	- `Content-Type: application/json`

- **Request body**
	- JSON in body
	- `"text": "<actual_query_text>"`

- **Response format**
	- JSON response
	
	- ```
	 {
		  "code": 200,
		  "data": {
			    "confidence": 0.69,
			    "hypothesis": "...",
			    "keywords_detected": "...",
			    "text": "..." 
		  },
		  "message": "It works!"
	}
	```
- **Example**
```
curl -X POST -H "auth_key: TheDayTheWorldWentAway" -H "Content-Type: application/json" \ 
-d '{ "text": "Random text" }' "https://samaritan-ai.herokuapp.com/api/" 
 ```