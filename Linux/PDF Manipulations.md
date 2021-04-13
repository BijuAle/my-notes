# PDF manipulations

## Convert JPG image to PDF
``` bash
convert <filename>.jpg -auto-orient <filename>.pdf
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
pdfgrep -r --include *.pdf <search-text>
```

## Trim first page
```bash
mkdir trimmed
for i in *pdf;
	do pdftk "$i" cat 2-end output "trimmed/$i";
done
```