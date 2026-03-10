import React from 'react';
import { PieChart, Pie, Cell, ResponsiveContainer, Tooltip as RechartsTooltip, Legend } from 'recharts';

const MemoryChart = ({ memoryData }) => {
    if (!memoryData) return null;

    // The backend provides string format like "8.5 GB". We need to parse this for the chart.
    const usedStr = memoryData.ram_used || "0 GB";
    const usedVal = parseFloat(usedStr.split(' ')[0]);
    
    const availableStr = memoryData.ram_available || "0 GB";
    const availableVal = parseFloat(availableStr.split(' ')[0]);

    const data = [
        { name: 'Used RAM', value: usedVal, color: '#3b82f6' }, // blue-500
        { name: 'Available RAM', value: availableVal, color: '#3f3f46' }, // zinc-700
    ];

    // Tooltip customized to add "GB"
    const CustomTooltip = ({ active, payload }) => {
        if (active && payload && payload.length) {
            return (
                <div className="bg-zinc-800 border border-zinc-700 p-2 rounded-lg text-xs shadow-xl">
                    <p className="text-zinc-300 font-semibold">{`${payload[0].name} : ${payload[0].value.toFixed(1)} GB`}</p>
                </div>
            );
        }
        return null;
    };

    return (
        <div className="w-full h-48 flex flex-col items-center justify-center bg-zinc-900 rounded-xl p-4 border border-zinc-800">
            <h3 className="text-zinc-400 text-sm font-semibold mb-1 w-full text-left">Memory (RAM)</h3>
            <div className="flex-1 w-full relative -mt-2">
                <ResponsiveContainer width="100%" height="100%">
                    <PieChart>
                        <Pie
                            data={data}
                            cx="50%"
                            cy="50%"
                            innerRadius={45}
                            outerRadius={65}
                            paddingAngle={5}
                            dataKey="value"
                            stroke="none"
                        >
                            {data.map((entry, index) => (
                                <Cell key={`cell-${index}`} fill={entry.color} />
                            ))}
                        </Pie>
                        <RechartsTooltip content={<CustomTooltip />} />
                    </PieChart>
                </ResponsiveContainer>
                {/* Center Text */}
                <div className="absolute inset-0 flex items-center justify-center flex-col top-2">
                    <span className="text-lg font-bold text-white tracking-tight">{memoryData.ram_percent}</span>
                    <span className="text-[10px] text-zinc-500">Used</span>
                </div>
            </div>
            
            {/* Custom Legend to save space */}
            <div className="flex justify-between w-full text-xs mt-2 px-2">
                 <div className="flex items-center gap-1">
                    <div className="w-2 h-2 rounded-full bg-blue-500"></div>
                    <span className="text-zinc-400">Used: {usedStr}</span>
                 </div>
                 <div className="flex items-center gap-1">
                    <div className="w-2 h-2 rounded-full bg-zinc-700"></div>
                    <span className="text-zinc-400">Free: {availableStr}</span>
                 </div>
            </div>
        </div>
    );
};

export default MemoryChart;
