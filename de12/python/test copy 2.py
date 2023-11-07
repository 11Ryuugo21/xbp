const ,translate, = require('google-translate-api'); または他の翻訳ライブラリ

選択したテキストを取得
const ,selectedText, = window.getSelection().toString();

テキストを翻訳
translate(selectedText,  souce_lang='ja', target_lang= 'en' )
then(result = {
    "翻訳されたテキストを挿入"
    window.document.execCommand('insertText', false, result.text);
  
  .catch(error => {
    console.error('翻訳エラー:', error);
  