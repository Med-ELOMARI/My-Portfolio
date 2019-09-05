# YoruserBeta.ClientsApi

All URIs are relative to *https://localhost:5000/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createANewClient**](ClientsApi.md#createANewClient) | **POST** /clients/ | Creates a new Client
[**deleteAClient**](ClientsApi.md#deleteAClient) | **DELETE** /clients/{client_name} | delete a Client
[**getAClient**](ClientsApi.md#getAClient) | **GET** /clients/{client_name} | get a Single client
[**listOfRegisteredClients**](ClientsApi.md#listOfRegisteredClients) | **GET** /clients/all | List all registered clients


<a name="createANewClient"></a>
# **createANewClient**
> createANewClient(payload)

Creates a new Client

### Example
```javascript
var YoruserBeta = require('yoruser__beta');
var defaultClient = YoruserBeta.ApiClient.instance;

// Configure API key authorization: Authorization
var Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

var apiInstance = new YoruserBeta.ClientsApi();

var payload = new YoruserBeta.ClientAddingRequest(); // ClientAddingRequest | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.createANewClient(payload, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**ClientAddingRequest**](ClientAddingRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="deleteAClient"></a>
# **deleteAClient**
> deleteAClient(clientName)

delete a Client

### Example
```javascript
var YoruserBeta = require('yoruser__beta');
var defaultClient = YoruserBeta.ApiClient.instance;

// Configure API key authorization: Authorization
var Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

var apiInstance = new YoruserBeta.ClientsApi();

var clientName = "clientName_example"; // String | a client name


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.deleteAClient(clientName, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientName** | **String**| a client name | 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="getAClient"></a>
# **getAClient**
> ClientInfo getAClient(clientName)

get a Single client

### Example
```javascript
var YoruserBeta = require('yoruser__beta');
var defaultClient = YoruserBeta.ApiClient.instance;

// Configure API key authorization: Authorization
var Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

var apiInstance = new YoruserBeta.ClientsApi();

var clientName = "clientName_example"; // String | a client name


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.getAClient(clientName, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientName** | **String**| a client name | 

### Return type

[**ClientInfo**](ClientInfo.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="listOfRegisteredClients"></a>
# **listOfRegisteredClients**
> [ClientInfo] listOfRegisteredClients()

List all registered clients

### Example
```javascript
var YoruserBeta = require('yoruser__beta');
var defaultClient = YoruserBeta.ApiClient.instance;

// Configure API key authorization: Authorization
var Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

var apiInstance = new YoruserBeta.ClientsApi();

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.listOfRegisteredClients(callback);
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**[ClientInfo]**](ClientInfo.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

