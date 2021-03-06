from django.db import models

# Create your models here.
class Test(models.Model):
	Destination_Port = models.FloatField()
	Flow_Duration = models.FloatField()
	Total_Fwd_Packets = models.FloatField()
	Total_Backward_Packets = models.FloatField()
	Total_Length_of_Fwd_Packets = models.FloatField()
	Total_Length_of_Bwd_Packets = models.FloatField()
	Fwd_Packet_Length_Max = models.FloatField()
	Fwd_Packet_Length_Min = models.FloatField()
	Fwd_Packet_Length_Mean = models.FloatField()
	Fwd_Packet_Length_Std = models.FloatField()
	Bwd_Packet_Length_Max = models.FloatField()
	Bwd_Packet_Length_Min = models.FloatField()
	Bwd_Packet_Length_Mean = models.FloatField()
	Bwd_Packet_Length_Std = models.FloatField()
	Flow_Bytes_Sec = models.FloatField()
	Flow_Packets_Sec = models.FloatField()
	Flow_IAT_Mean = models.FloatField()
	Flow_IAT_Std = models.FloatField()
	Flow_IAT_Max = models.FloatField()
	Flow_IAT_Min = models.FloatField()
	Fwd_IAT_Total = models.FloatField()
	Fwd_IAT_Mean = models.FloatField()
	Fwd_IAT_Std = models.FloatField()
	Fwd_IAT_Max = models.FloatField()
	Fwd_IAT_Min = models.FloatField()
	Bwd_IAT_Total = models.FloatField()
	Bwd_IAT_Mean = models.FloatField()
	Bwd_IAT_Std = models.FloatField()
	Bwd_IAT_Max = models.FloatField()
	Bwd_IAT_Min = models.FloatField()
	Fwd_PSH_Flags = models.FloatField()
	Bwd_PSH_Flags = models.FloatField()
	Fwd_URG_Flags = models.FloatField()
	Bwd_URG_Flags = models.FloatField()
	Fwd_Header_Length = models.FloatField()
	Bwd_Header_Length = models.FloatField()
	Fwd_Packets_Sec = models.FloatField()
	Bwd_Packets_Sec = models.FloatField()
	Min_Packet_Length = models.FloatField()
	Max_Packet_Length = models.FloatField()
	Packet_Length_Mean = models.FloatField()
	Packet_Length_Std = models.FloatField()
	Packet_Length_Variance = models.FloatField()
	FIN_Flag_Count = models.FloatField()
	SYN_Flag_Count = models.FloatField()
	RST_Flag_Count = models.FloatField()
	PSH_Flag_Count = models.FloatField()
	ACK_Flag_Count = models.FloatField()
	URG_Flag_Count = models.FloatField()
	CWE_Flag_Count = models.FloatField()
	ECE_Flag_Count = models.FloatField()
	Down_Up_Ratio = models.FloatField()
	Average_Packet_Size = models.FloatField()
	Avg_Fwd_Segment_Size = models.FloatField()
	Avg_Bwd_Segment_Size = models.FloatField()
	Fwd_Avg_Bytes_Bulk = models.FloatField()
	Fwd_Avg_Packets_Bulk = models.FloatField()
	Fwd_Avg_Bulk_Rate = models.FloatField()
	Bwd_Avg_Bytes_Bulk = models.FloatField()
	Bwd_Avg_Packets_Bulk = models.FloatField()
	Bwd_Avg_Bulk_Rate = models.FloatField()
	Subflow_Fwd_Packets = models.FloatField()
	Subflow_Fwd_Bytes = models.FloatField()
	Subflow_Bwd_Packets = models.FloatField()
	Subflow_Bwd_Bytes = models.FloatField()
	Init_Win_bytes_forward = models.FloatField()
	Init_Win_bytes_backward = models.FloatField()
	act_data_pkt_fwd = models.FloatField()
	min_seg_size_forward = models.FloatField()
	Active_Mean = models.FloatField()
	Active_Std = models.FloatField()
	Active_Max = models.FloatField()
	Active_Min = models.FloatField()
	Idle_Mean = models.FloatField()
	Idle_Std = models.FloatField()
	Idle_Max = models.FloatField()
	Idle_Min = models.FloatField()

