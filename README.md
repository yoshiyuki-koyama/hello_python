# hello_python
個人的なPython練習用リポジトリ

## 仮想環境の作り方(Windows PowerShell)
参考資料："パッケージの操作 - Learn | Microsoft"[^1]

### 仮想環境を作る
```
python -m venv env
```
(envは任意の名前でOK。仮想環境のフォルダ名になる。)

### 仮想環境に入る前の事前準備

PowerShellのスクリプトファイル(.ps1)を実行するために実行ポリシーの設定[^2]が必要となる。
#### PowerShell
こちらのサイト(https://www.python.jp/install/windows/venv.html )[^3]を参考に下記コマンドを実行する。
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```
※`-Scope`の設定次第(CurrentUserなど)では一度だけ実行すればOKだけど、セキュリティ面で心配だったので`Process`にした。
#### VisualStudioCode の統合ターミナル
こちらのサイト(https://attakei.net/blog/2019/windows-vscode-venv/ )[^4]を参考に設定。
一度下記設定をすれば、設定したWorkSpaceではVisualStudioCodeを立ち上げるだけで設定が反映される。
1. File -> Preference -> Settings -> WorkSpaceタブを選択
2. Terminal > Integrated > Env:Windows で　Edit in settings.json を選択して、下記のように追加。環境変数としてExecutionPolicyを設定している。
```
{
    "terminal.integrated.env.windows": {
        "PSExecutionPolicyPreference": "RemoteSigned"
    }
}
```
### 仮想環境に入る
```
.\env\Scripts\Activate.ps1
```

### 仮想環境から抜ける
```
deactivate
```

## VisualStudioCodeのデバッグ設定
Run and Debugアイコン -> "create a launch.json file." -> "Python File"でlaunch.jsonファイルが作成される。
この状態だと現在VisualStudioCodeで選択されているファイルがデバッグされるが、`__main__.py`などに固定したいときは
"configurations"の"program"のところで指定すると変更できる[^5][^6]。
例) `"program" : "${workspaceFolder}/src/__main__.py"`
(変更したとき時は"name"も変えた方がいいと思う)

## 参考
[^1]:パッケージの操作 - Learn (Pythonでプロジェクトを作成して管理する) : Microsoft
https://docs.microsoft.com/ja-jp/learn/modules/python-create-manage-projects/2-set-up-project

[^2]:実行ポリシーについて - PowerShell | Microsoft Docs : Microsoft
https://docs.microsoft.com/ja-jp/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.2

[^3]:仮想環境：Python環境構築ガイド(Windows環境のPython) : Python Japan
https://www.python.jp/install/windows/venv.html

[^4]:Windows版VisualStudioCodeで、スムーズvenvを使うための設定まとめ: attakei
https://attakei.net/blog/2019/windows-vscode-venv/

[^5]:Debugging in Visual Studio Code (Launch.json attributes) : Visual Studio Code Docs : Microsoft
https://code.visualstudio.com/docs/editor/debugging#_launchjson-attributes

[^6]:Visual Studio Code Variables Reference : Visual Studio Code Docs : Microsoft
https://code.visualstudio.com/docs/editor/variables-reference