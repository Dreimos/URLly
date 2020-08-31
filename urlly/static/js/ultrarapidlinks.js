function ClipboardCopy() {
    /* Get the text field */
    var copyText = document.getElementById("UrlInput");
    /* Select the text field */
    copyText.select();
    /*For mobile devices*/
    copyText.setSelectionRange(0, 99999); 
    /* Copy the text inside the text field */
    document.execCommand("copy");
}