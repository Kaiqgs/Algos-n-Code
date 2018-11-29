package CPUEmulador.CPU;

import CPUEmulador.Memory.Information;
import java.util.BitSet;
import java.util.function.Function;

/**
 *
 * @author Kai
 */
public final class Instruction {

    private int id;
    private String name;
    private Information code;
    private Information op;
    public Function<Instruction, Boolean> func;

    public Instruction(int id, String name, Information code)
    {
        this.name = name;
        this.id = id;
        this.code = code;
    }

    public Instruction(Instruction instruction)
    {
        this.name = instruction.getName();
        this.id = instruction.getId();
        this.code = instruction.getCode();
    }

    public void setFunctionality(Function<Instruction, Boolean> func)
    {
        this.func = func;
    }

    public Boolean execute()
    {
        System.out.println(name);
        return func.apply(this);
    }

    public void setOperand(Information op)
    {
        this.op = op;
    }

    public Information getOperand()
    {
        return op;
    }

    public int getId()
    {
        return id;
    }

    public String getName()
    {
        return name;
    }

    public Information getCode()
    {
        return code;
    }

}
