# 開発者向け

# branchの説明
## main
本番環境で動作

## develop
featureから上がってきた機能をテストする。
DEBUG=True
デプロイさせて問題なければmainにpull requestする

## feature
ローカル環境で動作確認を行う
機能開発を行う。ブランチの切り方は以下のようにする。
例）良いね機能を作成
feature/good
