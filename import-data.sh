echo "[INFO] Der input Ordner wird gelöscht
rm -rf input
echo "[INFO] Ein neuer input Ordner wird erstellt
mkdir input
echo "[INFO] In den input Ordner navigieren"
cd input
echo "[INFO] Mit wget über der GitHub URL den titanic csv Datensetz importieren"
wget https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/titanic.csv
echo "[INFO] Aus dem input Ordner raus navigieren"
cd ..
