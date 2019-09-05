# YoruserBeta.ModelApi

All URIs are relative to *https://localhost:5000/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteModel**](ModelApi.md#deleteModel) | **DELETE** /model/ | Delete Model
[**getModelAccuracyStatus**](ModelApi.md#getModelAccuracyStatus) | **GET** /model/accuracy | Get Model Accuracy
[**getModelStatus**](ModelApi.md#getModelStatus) | **GET** /model/ | Get Model Status
[**trainTheModelForASpecificClientBasedOnYourAuthorization**](ModelApi.md#trainTheModelForASpecificClientBasedOnYourAuthorization) | **POST** /model/ | Start Model Training


<a name="deleteModel"></a>
# **deleteModel**
> deleteModel()

Delete Model

### Example
```javascript
var YoruserBeta = require('yoruser__beta');
var defaultClient = YoruserBeta.ApiClient.instance;

// Configure API key authorization: Authorization
var Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

var apiInstance = new YoruserBeta.ModelApi();

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.deleteModel(callback);
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

<a name="getModelAccuracyStatus"></a>
# **getModelAccuracyStatus**
> getModelAccuracyStatus()

Get Model Accuracy

### Example
```javascript
var YoruserBeta = require('yoruser__beta');
var defaultClient = YoruserBeta.ApiClient.instance;

// Configure API key authorization: Authorization
var Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

var apiInstance = new YoruserBeta.ModelApi();

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.getModelAccuracyStatus(callback);
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

<a name="getModelStatus"></a>
# **getModelStatus**
> ModelInfo getModelStatus()

Get Model Status

### Example
```javascript
var YoruserBeta = require('yoruser__beta');
var defaultClient = YoruserBeta.ApiClient.instance;

// Configure API key authorization: Authorization
var Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

var apiInstance = new YoruserBeta.ModelApi();

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.getModelStatus(callback);
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ModelInfo**](ModelInfo.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="trainTheModelForASpecificClientBasedOnYourAuthorization"></a>
# **trainTheModelForASpecificClientBasedOnYourAuthorization**
> trainTheModelForASpecificClientBasedOnYourAuthorization()

Start Model Training

### Example
```javascript
var YoruserBeta = require('yoruser__beta');
var defaultClient = YoruserBeta.ApiClient.instance;

// Configure API key authorization: Authorization
var Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

var apiInstance = new YoruserBeta.ModelApi();

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.trainTheModelForASpecificClientBasedOnYourAuthorization(callback);
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

