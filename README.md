# stretchysearch
stretchysearch aka elasticsearch local macos dev playground

## run

```commandline
python3 install.py
./bin/elasticsearch
cd /Users/tim/code/stretchysearch/elasticsearch-8.1.0
# if it fails
# then run: rm -rf data

curl --cacert $ES_PATH_CONF/certs/http_ca.crt -u elastic https://localhost:9200
Enter host password for user 'elastic':
default password = changeme
```

## macos security certs

```commandline
cd stretchysearch/elasticsearch-8.1.0/config/certs
security export -p -t certs -k `security list-keychains -d system|cut -d '"' -f 2` -o certs/certs.pem
echo insecure >> ~/.curlrc
git config --global http.sslVerify false
HOMEBREW_CURLRC=1 brew reinstall openssl curl
sed -i '/^insecure$/d' ~/.curlrc
git config --global http.sslVerify true
```


```commandline

✅ Elasticsearch security features have been automatically configured!
✅ Authentication is enabled and cluster connections are encrypted.

ℹ️  Password for the elastic user (reset with `bin/elasticsearch-reset-password -u elastic`):
  Afxs8lck+LzDYo*9p3s1

ℹ️  HTTP CA certificate SHA-256 fingerprint:
  044efa5211ad110eac51e87d42d9644313edd4a5dfd46c5a4dba89fd067e8a86

ℹ️  Configure Kibana to use this cluster:
• Run Kibana and click the configuration link in the terminal when Kibana starts.
• Copy the following enrollment token and paste it into Kibana in your browser (valid for the next 30 minutes):
  eyJ2ZXIiOiI4LjEuMCIsImFkciI6WyIxOTIuMTY4LjEuNjc6OTIwMSJdLCJmZ3IiOiIwNDRlZmE1MjExYWQxMTBlYWM1MWU4N2Q0MmQ5NjQ0MzEzZWRkNGE1ZGZkNDZjNWE0ZGJhODlmZDA2N2U4YTg2Iiwia2V5IjoidkRuR2xYOEJ6eXdlTW5MVzd4eF86MzczQjJmeTBRTENqRThwalFzRUViZyJ9

ℹ️  Configure other nodes to join this cluster:
• On this node:
  ⁃ Create an enrollment token with `bin/elasticsearch-create-enrollment-token -s node`.
  ⁃ Uncomment the transport.host setting at the end of config/elasticsearch.yml.
  ⁃ Restart Elasticsearch.
• On other nodes:
  ⁃ Start Elasticsearch with `bin/elasticsearch --enrollment-token <token>`, using the enrollment token that you generated.

```











