# YoruserBeta.RecommendApi

All URIs are relative to *https://localhost:5000/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getRecommendation**](RecommendApi.md#getRecommendation) | **GET** /recommend/ | all Recommendation methods endpoint
[**recommendItemsToItem**](RecommendApi.md#recommendItemsToItem) | **GET** /recommend/item/{itemID}/items/ | Recommend items to item
[**recommendItemsToUser**](RecommendApi.md#recommendItemsToUser) | **GET** /recommend/user/{userID}/items/ | Recommend items to user
[**recommendUsersToItem**](RecommendApi.md#recommendUsersToItem) | **GET** /recommend/item/{itemID}/users/ | Recommend users to item
[**recommendUsersToUser**](RecommendApi.md#recommendUsersToUser) | **GET** /recommend/user/{userID}/users/ | Recommend users to user


<a name="getRecommendation"></a>
# **getRecommendation**
> getRecommendation(opts)

all Recommendation methods endpoint

Capable of recommending items (Recommend items to user, Recommend items to item) or users (Recommend users to item, Recommend users to user)

### Example
```javascript
var YoruserBeta = require('yoruser__beta');
var defaultClient = YoruserBeta.ApiClient.instance;

// Configure API key authorization: Authorization
var Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

var apiInstance = new YoruserBeta.RecommendApi();

var opts = { 
  'clientName': "clientName_example", // String | method to recommend with  - items_to_user - users_to_user - users_to_item - items_to_item 
  'method': "method_example", // String | a client name
  'input': "input_example", // String | ID of the user or item for which personalized recommendations are to be generated
  'count': "count_example", // String | Number of recommendations
  'metadata': "metadata_example" // String | include metadata in the response
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.getRecommendation(opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientName** | **String**| method to recommend with  - items_to_user - users_to_user - users_to_item - items_to_item  | [optional] 
 **method** | **String**| a client name | [optional] 
 **input** | **String**| ID of the user or item for which personalized recommendations are to be generated | [optional] 
 **count** | **String**| Number of recommendations | [optional] 
 **metadata** | **String**| include metadata in the response | [optional] 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="recommendItemsToItem"></a>
# **recommendItemsToItem**
> recommendItemsToItem(itemID, opts)

Recommend items to item

### Example
```javascript
var YoruserBeta = require('yoruser__beta');
var defaultClient = YoruserBeta.ApiClient.instance;

// Configure API key authorization: Authorization
var Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

var apiInstance = new YoruserBeta.RecommendApi();

var itemID = "itemID_example"; // String | 

var opts = { 
  'count': "count_example", // String | Number of recommendations
  'metadata': "metadata_example" // String | include metadata in the response
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.recommendItemsToItem(itemID, opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **itemID** | **String**|  | 
 **count** | **String**| Number of recommendations | [optional] 
 **metadata** | **String**| include metadata in the response | [optional] 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="recommendItemsToUser"></a>
# **recommendItemsToUser**
> recommendItemsToUser(userID, opts)

Recommend items to user

### Example
```javascript
var YoruserBeta = require('yoruser__beta');
var defaultClient = YoruserBeta.ApiClient.instance;

// Configure API key authorization: Authorization
var Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

var apiInstance = new YoruserBeta.RecommendApi();

var userID = "userID_example"; // String | 

var opts = { 
  'count': "count_example", // String | Number of recommendations
  'metadata': "metadata_example" // String | include metadata in the response
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.recommendItemsToUser(userID, opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userID** | **String**|  | 
 **count** | **String**| Number of recommendations | [optional] 
 **metadata** | **String**| include metadata in the response | [optional] 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="recommendUsersToItem"></a>
# **recommendUsersToItem**
> recommendUsersToItem(itemID, opts)

Recommend users to item

### Example
```javascript
var YoruserBeta = require('yoruser__beta');
var defaultClient = YoruserBeta.ApiClient.instance;

// Configure API key authorization: Authorization
var Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

var apiInstance = new YoruserBeta.RecommendApi();

var itemID = "itemID_example"; // String | 

var opts = { 
  'count': "count_example", // String | Number of recommendations
  'metadata': "metadata_example" // String | include metadata in the response
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.recommendUsersToItem(itemID, opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **itemID** | **String**|  | 
 **count** | **String**| Number of recommendations | [optional] 
 **metadata** | **String**| include metadata in the response | [optional] 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="recommendUsersToUser"></a>
# **recommendUsersToUser**
> recommendUsersToUser(userID, opts)

Recommend users to user

### Example
```javascript
var YoruserBeta = require('yoruser__beta');
var defaultClient = YoruserBeta.ApiClient.instance;

// Configure API key authorization: Authorization
var Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

var apiInstance = new YoruserBeta.RecommendApi();

var userID = "userID_example"; // String | 

var opts = { 
  'count': "count_example", // String | Number of recommendations
  'metadata': "metadata_example" // String | include metadata in the response
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.recommendUsersToUser(userID, opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userID** | **String**|  | 
 **count** | **String**| Number of recommendations | [optional] 
 **metadata** | **String**| include metadata in the response | [optional] 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

