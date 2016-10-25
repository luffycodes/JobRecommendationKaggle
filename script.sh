touch results
rm results
echo "MAP150 value for benchmark algorithm:" >> results
python popular_jobs_benchmark.py; python map150.py popular_jobs_benchmark.csv >> results
echo "MAP150 value for simple collaborative algorithm:" >> results
python popular_jobs_collaborative.py; python map150.py popular_jobs_collaborative.csv >> results
echo "MAP150 value for collaborative algorithm(with Jaccard Index)" >> results
python popular_jobs_jacard.py; python map150.py popular_jobs_jacard.csv >> results
echo "MAP150 value for collaborative algorithm(with Jaccard Index, user degree, major, experience)" >> results
python popular_jobs_jacard_adv.py; python map150.py popular_jobs_jacard_adv.csv >> results
