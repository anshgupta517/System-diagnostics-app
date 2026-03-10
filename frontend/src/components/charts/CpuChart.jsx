import React from 'react';
import { RadialBarChart, RadialBar, PolarAngleAxis, ResponsiveContainer } from 'recharts';

const CpuChart = ({ cpuData }) => {
    if (!cpuData) return null;

    // Parse the total CPU usage string (e.g. "45.2%") to a float
    const usageStr = cpuData.total_cpu_usage || "0%";
    const usageValue = parseFloat(usageStr.replace('%', ''));
    
    // Color logic: green < 50, yellow 50-80, red > 80
    let fillColor = '#10b981'; // tailwind emerald-500
    if (usageValue >= 80) fillColor = '#ef4444'; // tailwind red-500
    else if (usageValue >= 50) fillColor = '#eab308'; // tailwind yellow-500

    const data = [{
        name: 'CPU',
        value: usageValue,
        fill: fillColor
    }];

    return (
        <div className="w-full h-48 flex flex-col items-center justify-center bg-zinc-900 rounded-xl p-4 border border-zinc-800">
            <h3 className="text-zinc-400 text-sm font-semibold mb-2 w-full text-left">CPU Usage</h3>
            <div className="flex-1 w-full relative">
                <ResponsiveContainer width="100%" height="100%">
                    <RadialBarChart 
                        cx="50%" 
                        cy="50%" 
                        innerRadius="70%" 
                        outerRadius="100%" 
                        barSize={15} 
                        data={data}
                        startAngle={180}
                        endAngle={0}
                    >
                        <PolarAngleAxis
                            type="number"
                            domain={[0, 100]}
                            angleAxisId={0}
                            tick={false}
                        />
                        <RadialBar
                            minAngle={15}
                            background={{ fill: '#27272a' }} // tailwind zinc-800
                            clockWise
                            dataKey="value"
                            cornerRadius={10}
                        />
                    </RadialBarChart>
                </ResponsiveContainer>
                
                {/* Center Text */}
                <div className="absolute inset-0 flex items-center justify-center flex-col mt-4">
                    <span className="text-2xl font-bold text-white tracking-tight">{usageValue.toFixed(1)}%</span>
                    <span className="text-xs text-zinc-500">
                        {cpuData.cpu_count_logical} Cores
                    </span>
                </div>
            </div>
        </div>
    );
};

export default CpuChart;
