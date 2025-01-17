# change-off cuda
from . import nms_rotated_cpu

__all__ = ['nms_rotated']


def nms_rotated(dets, iou_thr):
    if dets.shape[0] == 0:
        return dets
    keep_inds = nms_rotated_cpu.nms_rotated(dets[:, :5], dets[:, 5], iou_thr)
    dets = dets[keep_inds, :]
    return dets, keep_inds
