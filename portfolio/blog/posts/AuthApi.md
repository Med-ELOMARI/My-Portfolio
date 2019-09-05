# YoruserBeta.AuthApi

All URIs are relative to *https://localhost:5000/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clientLogin**](AuthApi.md#clientLogin) | **POST** /auth/login | get Authorization key
[**logoutAClient**](AuthApi.md#logoutAClient) | **POST** /auth/logout | log out the Authorization key


<a name="clientLogin"></a>
# **clientLogin**
> clientLogin(payload)

get Authorization key

:return:

### Example
```javascript
var YoruserBeta = require('yoruser__beta');

var apiInstance = new YoruserBeta.AuthApi();

var payload = new YoruserBeta.LoginRequest(); // LoginRequest | 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.clientLogin(payload, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**LoginRequest**](LoginRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="logoutAClient"></a>
# **logoutAClient**
> logoutAClient()

log out the Authorization key

:return:

### Example
```javascript
var YoruserBeta = require('yoruser__beta');
var defaultClient = YoruserBeta.ApiClient.instance;

// Configure API key authorization: Authorization
var Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

var apiInstance = new YoruserBeta.AuthApi();

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
apiInstance.logoutAClient(callback);
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

