# hello_python
個人的なPython練習用リポジトリ

## 仮想環境の作り方(Windows PowerShell)
参考資料："パッケージの操作 - Learn | Microsoft"[^1]

### 仮想環境を作る(envは任意の名前でOK)
```
python -m venv env
```
### 仮想環境に入る前の事前準備
PowerShellのスクリプトファイル(.ps1)を実行するために下記コマンドを実行する[^2][^3]。
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```
※`-Scope`の設定次第(CurrentUserなど)では一度だけ実行すればOKだけど、セキュリティ面で心配だったので`Process`にした。


### 仮想環境に入る
```
.\env\Scripts\Activate.ps1
```

### 仮想環境から抜ける
```
deactivate
```

## 参考
[^1]パッケージの操作 - Learn (Pythonでプロジェクトを作成して管理する) : Microsoft
https://docs.microsoft.com/ja-jp/learn/modules/python-create-manage-projects/2-set-up-project

[^2]:仮想環境：Python環境構築ガイド(Windows環境のPython) : Python Japan
https://www.python.jp/install/windows/venv.html

[^3]:実行ポリシーについて - PowerShell | Microsoft Docs : Microsoft
https://docs.microsoft.com/ja-jp/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.2