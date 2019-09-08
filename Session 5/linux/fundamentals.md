# Linux Fundamentals

## Create a Collection of Files
create, extract or list contents of a tar archive using pattern, if supplied

`tar c|x|t -f tarfile [pattern]`

|tar Options|Description|
|--|--|
|`c`|create a tar archive|
|`x`|extract files from the archive|
|`t`|display the table of the contents (list)|
|`v`|be verbose|
|`z`|use compression (usually named `file.tar.gz` or `file.tgz`)|
|`f file`|use this file|

```bash
# bundle files
$ tar cf test.tar test/

# list contents
$ tar tf test.tar
test/
test/1.txt
test/2.txt
test/3.txt

# (verbose) extract
$ tar xvf test.tar
test/
test/1.txt
test/2.txt
test/3.txt
```

## Compress Files to Save Space
|Command|Description|
|--|--|
|`gzip`|compress file|
|`gunzip`|uncompress file|


### `tar` and `zip` Difference
`tar` in itself just bundles files together, while `zip` applies compression as well.

Usually you use `gzip` along with tar to compress the resulting tarball, thus achieving similar results as with `zip`.

For reasonably large archives there are important differences though. A zip archive is a catalog of compressed files. With a gzipped tar, it is a compressed catalog, of files. Thus a zip archive is a randomly accessible list of concatenated compressed items, and a `.tar.gz` is an archive that must be fully expanded before the catalog is accessible.

- The caveat of a `zip` is that **you don't get compression across files**.
- The caveat of a `.tar.gz` is that **you must decompress the whole archive**.

### How Compression Works
#### Lossy Compression
Lossy compression reduces file size by removing unnecessary bits of information. It’s most common in image, video, and audio formats, where a perfect representation of the source media isn’t necessary. Many common formats for these types of media use lossy compression; MP3 and JPEG are two popular examples.

An MP3 doesn’t contain all the audio information from the original recording—instead, it throws out some sounds that humans can’t hear. You wouldn’t notice them missing anyway, so removing that info results in a lower file size with basically no drawbacks.

Similarly, JPEGs remove non-vital parts of images. For instance, in a picture containing a blue sky, JPEG compression might change all the sky pixels to one or two shades of blue, instead of using dozens of different shades.

But lossy compression doesn’t work so well for files where all the information is crucial. For instance, using lossy compression on a text file or a spreadsheet would result in garbled output. You really can’t throw anything out without severely harming the final product.

#### Lossless Compression
Lossless compression is a way of reducing file size so that you can perfectly reconstruct the original file. Contrary to lossy compression, it doesn’t throw any information out. Instead, lossless compression essentially works by removing redundancy.

![Lossless Before](./lossless_before.jpg =150x200)
![Lossless After](./lossless_after.jpg =150x200)

```
mmmmmuuuuuuuoooooooooooo

m5u7o12
```

When you create a ZIP file from a program executable, it uses lossless compression. The ZIP file compression is a more efficient way to store the program, but when you unzip (decompress) it, all the original information is present. If you used lossy compression to compress executables, the unzipped version would be damaged and unusable.

Common lossless formats include PNG for images, FLAC for audio, and ZIP. Lossless formats for video are rare, because they would take up massive amounts of space.

Notes:
- Converting lossy formats to lossless is simply a waste of space. Remember that lossy formats throw data out; it’s impossible to recover that data.

- Converting one lossy format to another (or repeatedly saving in the same format) will degrade the quality further. Every time you apply the lossy compression, you lose more detail. This becomes more and more noticeable until the file is essentially ruined

