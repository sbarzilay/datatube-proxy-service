import json
import re
import statistics

from azure.kusto.data.response import KustoResponseDataSetV2

if __name__ == '__main__':
	file_name = '/Users/talshel/playground/ab/output2.txt'
	data = [line for line in open(file_name, 'r') if 'ExecutionTime' in line]
	execution_times = []
	for row in data:
		execution_time = re.search(r"ExecutionTime\\\":(\d+.\d+),", row, re.IGNORECASE)

		if execution_time:
			execution_times.append(float(execution_time.group(1)))

	assert len(execution_times) == len(data)
	print(f'mean is {statistics.mean(execution_times)}')
	print(f'median is {statistics.median(execution_times)}')
	print()
	for i, t in enumerate(sorted(execution_times)):
		print(f'#{i} - {t:0.2f}')
