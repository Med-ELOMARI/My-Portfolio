# YoruserBeta.UploadPayload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **String** | A Csv file , Max size 20971520 Byte | 
**type** | **String** | csv file type , can be users , items  or interactions (case sensitive*) | 
**idColumnName** | **String** | column name where the IDs are located , in the  interactions case , give both columns of users and items separated by + (ex : USER_ID+ITEMS_ID) | 
**features** | **String** | column names where the features are  located , those features will be used by the ML model of users and items separated by + (ex : Age+Location) for interactions give the interactions column name  | [optional] 


