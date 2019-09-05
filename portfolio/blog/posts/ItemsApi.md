# YoruserBeta.ItemsApi

All URIs are relative to *https://localhost:5000/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addItems_**](ItemsApi.md#addItems_) | **POST** /items/ | Add new items
[**deleteAnItemForAClient**](ItemsApi.md#deleteAnItemForAClient) | **DELETE** /items/ | delete an item
[**getItemsInfoForClient**](ItemsApi.md#getItemsInfoForClient) | **GET** /items/ | get items info


<a name="addItems_"></a>
# **addItems_**
> addItems_(payload)

Add new items

### Example
```javascript
var YoruserBeta = require('yoruser__beta');
var defaultClient = YoruserBeta.ApiClient.instance;

// Configure API key authorization: Authorization
var Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

var apiInstance = new YoruserBeta.ItemsApi();

var payload = new YoruserBeta.ItemsList(); // ItemsList | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.addItems_(payload, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**ItemsList**](ItemsList.md)|  | 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="deleteAnItemForAClient"></a>
# **deleteAnItemForAClient**
> deleteAnItemForAClient()

delete an item

### Example
```javascript
var YoruserBeta = require('yoruser__beta');
var defaultClient = YoruserBeta.ApiClient.instance;

// Configure API key authorization: Authorization
var Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

var apiInstance = new YoruserBeta.ItemsApi();

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.deleteAnItemForAClient(callback);
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="getItemsInfoForClient"></a>
# **getItemsInfoForClient**
> getItemsInfoForClient()

get items info

### Example
```javascript
var YoruserBeta = require('yoruser__beta');
var defaultClient = YoruserBeta.ApiClient.instance;

// Configure API key authorization: Authorization
var Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

var apiInstance = new YoruserBeta.ItemsApi();

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.getItemsInfoForClient(callback);
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

