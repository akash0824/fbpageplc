# fbpageplc
Fetch posts, likes, comments of a public facebook page. It is a python package used to get posts data from  facebook public page.

## Following are three functions which can be used:


### Getting posts form a public page
#### get_posts(pagename, access_token, start_date, end_date)

pagename - Given name of the public page e.g. BPAmerica (note: if url of page is "https://www.facebook.com/BPAmerica/" then "BPAmerica" will be the pagename).

access_token - For this one should have facebook account. Login to facebook account, and open the following url "https://developers.facebook.com/tools/explorer", copy the access token.

start_date - Specifies date from which date you want to gather the posts.

end_date - Specifies date till which date you want to gather the posts.

note : if start_date and end_date are not given then by default all the posts will be gathered. one can give end_date as "now".

#### output 
Returns a list of json objects. Each json object contains : id, message, created_time


### Getting likes of a public page's post
#### get_likes(post_id, access_token)

post_id - Unique id of a public page's post. same id returned by get_posts method inside json object. 

access_token - For this one should have facebook account. Login to facebook account, and open the following url "https://developers.facebook.com/tools/explorer", copy the access token.

#### output

Returns a list of json objects. Each json object contains : id, name

### Getting comments of a public page's post
#### get_comments(post_id, access_token)

post_id - Unique id of a public page's post. same id returned by get_posts method inside json object. 

access_token - For this one should have facebook account. Login to facebook account, and open the following url "https://developers.facebook.com/tools/explorer", copy the access token.

#### output

Returns a list of json objects. Each json object contains : id, message, from.id, from.name, created_time


