import React, { useState } from 'react';
import { Send, Loader2 } from 'lucide-react';

const InputBox = ({ onSend, disabled }) => {
    const [input, setInput] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        if (input.trim() && !disabled) {
            onSend(input);
            setInput('');
        }
    };

    return (
        <form onSubmit={handleSubmit} className="relative w-full">
            <input
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                placeholder="Why is my system slow?"
                disabled={disabled}
                className="w-full bg-zinc-800 text-white placeholder-zinc-500 rounded-xl pl-4 pr-12 py-4 border border-zinc-700 focus:border-blue-500 focus:ring-1 focus:ring-blue-500 outline-none transition-all"
            />
            <button
                type="submit"
                disabled={!input.trim() || disabled}
                className="absolute right-2 top-1/2 -translate-y-1/2 p-2 text-zinc-400 hover:text-white disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
            >
                {disabled ? <Loader2 className="animate-spin w-5 h-5" /> : <Send className="w-5 h-5" />}
            </button>
        </form>
    );
};

export default InputBox;
