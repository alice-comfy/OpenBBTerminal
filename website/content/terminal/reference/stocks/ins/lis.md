---
title: lis
description: OpenBB Terminal Function
---

# lis

Print latest insider sales. [Source: OpenInsider]

### Usage

```python
lis [-l LIMIT]
```

---

## Parameters

| Name | Description | Default | Optional | Choices |
| ---- | ----------- | ------- | -------- | ------- |
| limit | Limit of datarows to display | 10 | True | None |


---

## Examples

```python
2022 Feb 16, 07:56 (🦋) /stocks/ins/ $ lis
                                                                               Insider Data
┏━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━┓
┃ X ┃ Filing Date ┃ Trade Date ┃ Ticker ┃ Company Name         ┃ Insider Name        ┃ Title      ┃ Trade Type  ┃ Price   ┃ Qty     ┃ Owned     ┃ Diff Own ┃ Value       ┃
┡━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━┩
│ D │ 2022-02-15  │ 2022-02-14 │ BVS    │ Bioventus Inc.       │ D'Adamio Anthony    │ SVP, GC    │ S - Sale+OE │ $11.99  │ -1,294  │ 18,672    │ -6%      │ -$15,513    │
│   │ 21:31:03    │            │        │                      │                     │            │             │         │         │           │          │             │
├───┼─────────────┼────────────┼────────┼──────────────────────┼─────────────────────┼────────────┼─────────────┼─────────┼─────────┼───────────┼──────────┼─────────────┤
│ D │ 2022-02-15  │ 2022-02-14 │ BVS    │ Bioventus Inc.       │ Anglum Gregory O.   │ SVP, CFO   │ S - Sale+OE │ $11.99  │ -1,294  │ 55,013    │ -2%      │ -$15,518    │
│   │ 21:27:43    │            │        │                      │                     │            │             │         │         │           │          │             │
├───┼─────────────┼────────────┼────────┼──────────────────────┼─────────────────────┼────────────┼─────────────┼─────────┼─────────┼───────────┼──────────┼─────────────┤
│ D │ 2022-02-15  │ 2022-02-14 │ BVS    │ Bioventus Inc.       │ Nosenzo John        │ Chief      │ S - Sale+OE │ $11.99  │ -534    │ 43,370    │ -1%      │ -$6,401     │
│   │ 21:17:44    │            │        │                      │                     │ Commercial │             │         │         │           │          │             │
│   │             │            │        │                      │                     │ Officer    │             │         │         │           │          │             │
├───┼─────────────┼────────────┼────────┼──────────────────────┼─────────────────────┼────────────┼─────────────┼─────────┼─────────┼───────────┼──────────┼─────────────┤
│ D │ 2022-02-15  │ 2022-02-11 │ PGNY   │ Progyny, Inc.        │ Schlanger David J   │ Exec COB   │ S - Sale+OE │ $42.00  │ -1,000  │ 84,000    │ -1%      │ -$42,000    │
│   │ 21:09:05    │            │        │                      │                     │            │             │         │         │           │          │             │
├───┼─────────────┼────────────┼────────┼──────────────────────┼─────────────────────┼────────────┼─────────────┼─────────┼─────────┼───────────┼──────────┼─────────────┤
│ D │ 2022-02-15  │ 2022-02-15 │ EW     │ Edwards Lifesciences │ Mussallem Michael A │ COB, CEO   │ S - Sale+OE │ $110.09 │ -32,550 │ 3,820,007 │ -1%      │ -$3,583,289 │
│   │ 20:50:39    │            │        │ Corp                 │                     │            │             │         │         │           │          │             │
├───┼─────────────┼────────────┼────────┼──────────────────────┼─────────────────────┼────────────┼─────────────┼─────────┼─────────┼───────────┼──────────┼─────────────┤
│ D │ 2022-02-15  │ 2022-02-11 │ AGCO   │ Agco Corp /de        │ Beck Andrew H       │ SVP, CFO   │ S - Sale+OE │ $131.83 │ -25,000 │ 107,337   │ -19%     │ -$3,295,750 │
│   │ 20:38:48    │            │        │                      │                     │            │             │         │         │           │          │             │
├───┼─────────────┼────────────┼────────┼──────────────────────┼─────────────────────┼────────────┼─────────────┼─────────┼─────────┼───────────┼──────────┼─────────────┤
│ D │ 2022-02-15  │ 2022-02-14 │ PUBM   │ Pubmatic, Inc.       │ Goel Amar K.        │ Chief      │ S - Sale+OE │ $29.85  │ -24,000 │ 0         │ -100%    │ -$716,444   │
│   │ 20:24:51    │            │        │                      │                     │ Innovation │             │         │         │           │          │             │
│   │             │            │        │                      │                     │ Officer,   │             │         │         │           │          │             │
│   │             │            │        │                      │                     │ 10%        │             │         │         │           │          │             │
├───┼─────────────┼────────────┼────────┼──────────────────────┼─────────────────────┼────────────┼─────────────┼─────────┼─────────┼───────────┼──────────┼─────────────┤
│ D │ 2022-02-15  │ 2022-02-14 │ NET    │ Cloudflare, Inc.     │ Meresman Stanley J  │ Dir        │ S - Sale+OE │ $106.00 │ -18,622 │ 2,441     │ -88%     │ -$1,973,993 │
│   │ 19:57:51    │            │        │                      │                     │            │             │         │         │           │          │             │
├───┼─────────────┼────────────┼────────┼──────────────────────┼─────────────────────┼────────────┼─────────────┼─────────┼─────────┼───────────┼──────────┼─────────────┤
│ D │ 2022-02-15  │ 2022-02-14 │ AON    │ Aon Plc              │ Davies Christa      │ CFO        │ S - Sale+OE │ $283.72 │ -616    │ 200,237   │ 0%       │ -$174,772   │
│   │ 19:36:49    │            │        │                      │                     │            │             │         │         │           │          │             │
├───┼─────────────┼────────────┼────────┼──────────────────────┼─────────────────────┼────────────┼─────────────┼─────────┼─────────┼───────────┼──────────┼─────────────┤
│ D │ 2022-02-15  │ 2022-02-15 │ RYTM   │ Rhythm               │ Shulman Joseph      │ Chief      │ S - Sale+OE │ $6.10   │ -557    │ 1,006     │ -36%     │ -$3,398     │
│   │ 19:32:08    │            │        │ Pharmaceuticals,     │                     │ Technical  │             │         │         │           │          │             │
│   │             │            │        │ Inc.                 │                     │ Officer    │             │         │         │           │          │             │
└───┴─────────────┴────────────┴────────┴──────────────────────┴─────────────────────┴────────────┴─────────────┴─────────┴─────────┴───────────┴──────────┴─────────────┘
D: Derivative transaction in filing (usually option exercise)
```
---