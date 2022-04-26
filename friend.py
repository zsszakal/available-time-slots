import  helpers as h
from timerange import TimeRange
from dataclasses import dataclass, field

@dataclass
class Friend:
    name: str
    busy_time_ranges: list[TimeRange] = field(default_factory=list, repr=False)

    def add_busy_range(self, obj:TimeRange):
        self.busy_time_ranges.append(obj)

f1 = Friend("Jim")
f1.add_busy_range(TimeRange(start_time="09:00", end_time="17:00"))
f1.add_busy_range(TimeRange(start_time="18:00", end_time="23:00"))
print(f1.busy_time_ranges)
print(f1)