# Basic-Hash-Collision-Trojan-Program
This is a basic trojan horse program utilizing an MD5 hash collision. MD5 is a weak encryption algorithm with a known hash collision vulnerability. The point of this program is to show how a hash collision can be used to create a trojan horse, not to show the weakness of the MD5 encryption algorithm. This was a bonus assignment for my college cryptography course using Marc Steven's Fastcol v1.0.0.5 (https://www.win.tue.nl/hashclash/) to generate the md5 hash collision. There are two programs in this repository, named  "good.py" and "evil.py" respectively. Both of these programs have the same md5 hash, different sha256 hashes and will output different text (behave differently) based on their sha256 hashes. When run the good program will output "I come in peace." and the evil program will output "Prepare to be destroyed!"

Most of the files for this program might not be viewable in github due to the encoding. 


Two messages
```
Message 1:
d131dd02c5e6eec4693d9a0698aff95c 2fcab58712467eab4004583eb8fb7f89
55ad340609f4b30283e488832571415a 085125e8f7cdc99fd91dbdf280373c5b
d8823e3156348f5bae6dacd436c919c6 dd53e2b487da03fd02396306d248cda0
e99f33420f577ee8ce54b67080a80d1e c69821bcb6a8839396f9652b6ff72a70
```
```
Message 2:
d131dd02c5e6eec4693d9a0698aff95c 2fcab50712467eab4004583eb8fb7f89
55ad340609f4b30283e4888325f1415a 085125e8f7cdc99fd91dbd7280373c5b
d8823e3156348f5bae6dacd436c919c6 dd53e23487da03fd02396306d248cda0
e99f33420f577ee8ce54b67080280d1e c69821bcb6a8839396f965ab6ff72a70
```


Were converted into binary using

`xxd -r -p filename.hex > file`
  
then using openssl we can compare the digest for the different programs.

`openssl dgst -md5 file1 file2`
```
MD5(newcol1)= 1ba42b3162fd5b2c3c7338e36fa44e73
MD5(newcol2)= 1ba42b3162fd5b2c3c7338e36fa44e73
```
  
`openssl dgst -sha256 file1 file2`
```
SHA256(newcol1)= c43ea3f51f15537d4d4f0a96cd29e11523d50d08e23b178e1ba1a7721b947185
SHA256(newcol2)= 3db990ff36460b029044cda18f89d33e8900717e66b626c94e022ede7d3f8870
```
  
the digest of each file was compared to verify that the md5 hashes for these files matches and the sha256 did not match.
After that fastcol was used to generate the prefix then the suffix was appended to the programs with cat.

`fastcoll -p prefix -o col1 col2`
  
`cat col1 suffix > file1.py`
  
`cat col2 suffix > file2.py`
