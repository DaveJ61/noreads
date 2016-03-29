date;
echo READS;
grep -oh ID.....S TOTE-CNV*.log | sort | uniq -c;
echo NOREADS;
grep -oh ID.....S? TOTE-CNV*.log | sort | uniq -c;
echo END

