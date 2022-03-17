import os

if __name__ == "__main__":
    print("Running install.py")

    # download elasticsearch v8.1.0
    elastic_v_810 = "wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.1.0-darwin-aarch64.tar.gz"
    elastic_v_810_sha = "wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.1.0-darwin-aarch64.tar.gz.sha512"
    compare_shas = "shasum -a 512 -c elasticsearch-8.1.0-darwin-aarch64.tar.gz.sha512"
    un_archive = "tar -xzf elasticsearch-8.1.0-darwin-aarch64.tar.gz"

    print("Downloading elasticsearch-8.1.0-darwin-aarch64")
    os.system(elastic_v_810)
    os.system(elastic_v_810_sha)

    print("Installing..")
    os.system(compare_shas)
    os.system(un_archive)

    print("Finished running install.py")
