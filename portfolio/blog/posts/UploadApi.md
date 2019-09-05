# YoruserBeta.UploadApi

All URIs are relative to *https://localhost:5000/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteUserDataCsvFile_**](UploadApi.md#deleteUserDataCsvFile_) | **DELETE** /upload/ | Delete all csv files
[**listOfRegisteredClients**](UploadApi.md#listOfRegisteredClients) | **GET** /upload/ | check if uploaded
[**uploadDataCsvFileUsersItemsOrInteractions**](UploadApi.md#uploadDataCsvFileUsersItemsOrInteractions) | **POST** /upload/ | upload csv file (replace if exist)


<a name="deleteUserDataCsvFile_"></a>
# **deleteUserDataCsvFile_**
> deleteUserDataCsvFile_()

Delete all csv files

### Example
```javascript
var YoruserBeta = require('yoruser__beta');
var defaultClient = YoruserBeta.ApiClient.instance;

// Configure API key authorization: Authorization
var Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

var apiInstance = new YoruserBeta.UploadApi();

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.deleteUserDataCsvFile_(callback);
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

<a name="listOfRegisteredClients"></a>
# **listOfRegisteredClients**
> [DataSetInfo] listOfRegisteredClients()

check if uploaded

### Example
```javascript
var YoruserBeta = require('yoruser__beta');
var defaultClient = YoruserBeta.ApiClient.instance;

// Configure API key authorization: Authorization
var Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

var apiInstance = new YoruserBeta.UploadApi();

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

[**[DataSetInfo]**](DataSetInfo.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="uploadDataCsvFileUsersItemsOrInteractions"></a>
# **uploadDataCsvFileUsersItemsOrInteractions**
> uploadDataCsvFileUsersItemsOrInteractions(payload)

upload csv file (replace if exist)

### Example
```javascript
var YoruserBeta = require('yoruser__beta');
var defaultClient = YoruserBeta.ApiClient.instance;

// Configure API key authorization: Authorization
var Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

var apiInstance = new YoruserBeta.UploadApi();

var payload = new YoruserBeta.UploadPayload(); // UploadPayload | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.uploadDataCsvFileUsersItemsOrInteractions(payload, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**UploadPayload**](UploadPayload.md)|  | 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

