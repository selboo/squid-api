#Squid 删除缓存 API

## URL

>http://192.168.1.100/test.html

## HTTP请求方式
POST

## 请求参数

| 参数 | 类型 | 说明 |
| ------------- |:-------------:| -----:|
| type | string | 值必须为 purge |
| url | string | 值必须为标准完整URL 需携带 http |

## 案例 
> curl -d 'type=purge&url=http://192.168.1.100/test.html' http://127.0.0.1/cache

## 返回结果
>JSON示例

`
{
  "total": 33,
  "Success": 26,
  "Failure": 7,
}
`

## 返回字段说明

| 返回值| 类型 | 说明 |
| ------------- |:-------------:| -----:|
| total| int| squid服务器数量 |
| Success| int| 删除 成功 数量 |
| Failure| int|删除 失败 数量|

## 超时

>目前设置 超过 3 秒,就算失败
