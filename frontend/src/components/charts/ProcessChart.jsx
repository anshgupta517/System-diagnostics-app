import React, { useState } from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, ResponsiveContainer, Tooltip, Cell, LabelList } from 'recharts';

const ProcessChart = ({ processData }) => {
    if (!processData) return null;
    
    // Toggle between CPU and Memory view
    const [view, setView] = useState('cpu'); // 'cpu' or 'memory'

    const data = view === 'cpu' 
        ? processData.top_cpu_processes 
        : processData.top_memory_processes;

    const formatData = data?.map(proc => ({
        name: proc.name.length > 12 ? proc.name.substring(0, 10) + '...' : proc.name,
        fullName: proc.name,
        value: view === 'cpu' ? proc.cpu_percent : proc.memory_percent,
        pid: proc.pid
    })) || [];

    const CustomTooltip = ({ active, payload }) => {
        if (active && payload && payload.length) {
            const dataPoint = payload[0].payload;
            return (
                <div className="bg-zinc-800 border border-zinc-700 p-3 rounded-lg text-xs shadow-xl z-50">
                    <p className="text-white font-bold mb-1">{dataPoint.fullName}</p>
                    <p className="text-zinc-400">PID: {dataPoint.pid}</p>
                    <p className="text-zinc-300 font-semibold mt-1">
                        {view === 'cpu' ? 'CPU' : 'Memory'}: {dataPoint.value.toFixed(1)}%
                    </p>
                </div>
            );
        }
        return null;
    };

    return (
        <div className="w-full h-56 flex flex-col bg-zinc-900 rounded-xl p-4 border border-zinc-800 mt-2">
            <div className="flex justify-between items-center mb-4">
                <h3 className="text-zinc-400 text-sm font-semibold">Top Processes</h3>
                <div className="flex bg-zinc-950 rounded-lg p-1 border border-zinc-800">
                    <button 
                        onClick={() => setView('cpu')}
                        className={`text-[10px] px-2 py-1 rounded-md transition-colors ${view === 'cpu' ? 'bg-blue-600/20 text-blue-400' : 'text-zinc-500 hover:text-zinc-300'}`}
                    >
                        CPU
                    </button>
                    <button 
                        onClick={() => setView('memory')}
                        className={`text-[10px] px-2 py-1 rounded-md transition-colors ${view === 'memory' ? 'bg-purple-600/20 text-purple-400' : 'text-zinc-500 hover:text-zinc-300'}`}
                    >
                        RAM
                    </button>
                </div>
            </div>
            
            <div className="flex-1 w-full text-xs">
                <ResponsiveContainer width="100%" height="100%">
                    <BarChart
                        data={formatData}
                        layout="vertical"
                        margin={{ top: 0, right: 35, left: 0, bottom: 0 }}
                    >
                        <CartesianGrid strokeDasharray="3 3" horizontal={false} stroke="#3f3f46" vertical={false} />
                        <XAxis type="number" hide />
                        <YAxis 
                            dataKey="name" 
                            type="category" 
                            axisLine={false} 
                            tickLine={false} 
                            tick={{ fill: '#a1a1aa', fontSize: 10 }}
                            width={80}
                        />
                        <Tooltip content={<CustomTooltip />} cursor={{fill: '#27272a'}} />
                        <Bar dataKey="value" radius={[0, 4, 4, 0]} barSize={16}>
                             {formatData.map((entry, index) => (
                                <Cell key={`cell-${index}`} fill={view === 'cpu' ? '#3b82f6' : '#a855f7'} /> // blue-500 or purple-500
                            ))}
                            <LabelList 
                                dataKey="value" 
                                position="right" 
                                formatter={(val) => `${val.toFixed(1)}%`}
                                style={{ fill: '#d4d4d8', fontSize: 10 }} // zinc-300
                            />
                        </Bar>
                    </BarChart>
                </ResponsiveContainer>
            </div>
        </div>
    );
};

export default ProcessChart;
