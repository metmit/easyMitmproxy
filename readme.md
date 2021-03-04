# MitmProxy

使用`MitmProxy`截获网络请求的响应结果，将响应结果推送至服务端。

## 安装
```
$ sudo pip3 install mitmproxy
```

## 证书

生成证书，并信任该证书。
```
$ mitmdump
$ ls ~/.mitmproxy
```

**IOS**或**安卓7以下**的手机：

手机设置代理为当前IP & Port，浏览器访问`mitm.it`下载对应系统的证书，安装证书并信任，即可拦截HTTPS请求。

**安卓7以上**的手机：

1、查看证书的hash值，第一行的8个16进制即是，比如：c8750f0d
```
$ openssl x509 -inform PEM -subject_hash_old -in  ~/.mitmproxy/mitmproxy-ca-cert.pem
```

2、将证书拷贝为`c8750f0d.0`（后缀是数字0）
```
$ cp ~/.mitmproxy/mitmproxy-ca-cert.pem c8750f0d.0
```

3、将证书文件写入到Android的系统证书列表
```
$ adb root 
$ adb remount
$ adb shell rm -f /system/etc/security/cacerts/c8750f0d.0
$ adb push c8750f0d.0 /system/etc/security/cacerts/c8750f0d.0
```

## 启动
```
$ mitmdump -s loader.py -p 18888 -q
```