#include <iostream>
#include <algorithm>
#include <map>
#include <vector>

using namespace std;
typedef std::map<int, int>::value_type set_value_type;

int GetRanges(std::vector<int> numbers)
{
	int numRange = numbers.size();
	std::map<int, int> mapRange;
	int curNum = 0;
	auto findInRange = [&](const set_value_type& valType)->bool
	{
		if (curNum >= valType.first && curNum <= valType.second) return true;
		return false;
	};

	auto findFirstRange = [&](const set_value_type& valType)->bool
	{
		if (curNum - 1 == valType.second) return true;
		return false;
	};

	auto findSecondRange = [&](const set_value_type& valType)->bool
	{
		if (curNum + 1 == valType.first) return true;
		return false;
	};

	for (auto iter : numbers)
	{
		curNum = iter;
		auto iterRange = std::find_if(mapRange.begin(), mapRange.end(), findInRange);

		if (iterRange == mapRange.end())
		{
			auto iterFirstRange = std::find_if(mapRange.begin(), mapRange.end(), findFirstRange);
			auto iterSecondRange = std::find_if(mapRange.begin(), mapRange.end(), findSecondRange);
			if (iterFirstRange != mapRange.end() && iterSecondRange != mapRange.end())
			{
				iterFirstRange->second = iterSecondRange->second;
				mapRange.erase(iterSecondRange);
			}
			else if (iterFirstRange != mapRange.end())
			{
				++(iterFirstRange->second);
			}
			else if (iterSecondRange != mapRange.end())
			{
				mapRange.emplace(curNum, iterSecondRange->second);
				mapRange.erase(iterSecondRange);
			}
			else
			{
				mapRange.emplace(curNum, curNum);
			}
		}
	}
	for(auto elem : mapRange)
{
   std::cout << "("<<elem.first << "," << elem.second<<")";
}
    std:cout <<"\n";
	return mapRange.size();
}

int main()
{
	std::vector<int> v;
	v.push_back(1);
	GetRanges(v);
	v.push_back(5);
	v.push_back(2);
	GetRanges(v);
	v.push_back(6);
	v.push_back(4);
	GetRanges(v);
	//cout << "Current number of ranges = " << GetRanges(v) << endl;
	v.push_back(3);
	//cout << "Current number of ranges = " << GetRanges(v) << endl;
	v.push_back(8);
	GetRanges(v);
	v.push_back(10);
	//cout << "Current number of ranges = " << GetRanges(v) << endl;
	v.push_back(9);
	GetRanges(v);
	//cout << "Current number of ranges = " << GetRanges(v) << endl;
	v.push_back(7);
	//cout << "Current number of ranges = " << GetRanges(v) << endl;
	GetRanges(v);
	getchar();
	return 0;
}