## Docker Command

```
docker-compose up -d
docker-compose stop #コンテナ停止/GUI設定保持
docker-compose down #コンテナ削除
docker-compose down --volumes #DB含め削除
```

## ライブラリ管理

- 必要なライブラリを requirements.txt に追記
- コンテナをリビルド(← コマンドパレット)
