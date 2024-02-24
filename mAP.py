from evaluate.lvvis import LVVIS
from evaluate.lvviseval import LVVISeval

gt_path = 'datasets/LVVIS/val/val_instances.json'
dt_path = 'output/inference/results.json'

ytvosGT = LVVIS(gt_path)
ytvosDT = ytvosGT.loadRes(dt_path)
ytvosEval = LVVISeval(ytvosGT, ytvosDT, "segm")
ytvosEval.evaluate()
ytvosEval.accumulate()
ytvosEval.summarize()


