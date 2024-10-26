# PDF manipulations

## Convert JPG image to PDF
``` bash
for i in *jpeg; do
	convert "$i" -auto-orient name>.pdf
done

```
## Combine Images to PDF

```bash
convert *.jpg -auto-orient pictures.pdf
```
## Resize PDF to A4-paper

```bash
for pdf in *; do
	pdfjam --outfile $pdf --paper a4paper $pdf
done
```
## Search text within PDF
```bash
pdfgrep -C 3 -HiR -e Theseaus *.pdf
```
## Trim first page
```bash
mkdir trimmed
for i in *pdf;
	do pdftk "$i" cat 2-end output "trimmed/$i";
done
```
## Extract Images from PDF

```bash
mkdir extracted-images
pdfimages -all <path-to-pdf> <path-to-'extracted-images'>/image
```

## Multiple djvu to pdf
```bash 
for i in *.djvu; 
	do djvu2pdf "$i" "${i/%.djvu/}.pdf";
done
```